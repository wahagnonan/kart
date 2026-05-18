import csv
import json
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, JsonResponse
from django.contrib import messages
from django.views.decorators.http import require_POST
from .models import Question, Artisan, Reponse

VILLES = ['Abidjan', 'Bouaké', 'Daloa', 'San-Pédro', 'Yamoussoukro',
          'Korhogo', 'Man', 'Gagnoa', 'Autre']

METIERS = ['Menuisier', 'Maçon', 'Électricien', 'Plombier',
           'Coiffeur/Coiffeuse', 'Couturier/Couturière', 'Mécanicien',
           'Soudeur', 'Peintre', 'Teinturier', 'Cordonnier', 'Autre']


# ─── Dashboard ────────────────────────────────────────────────────────────────

def dashboard(request):
    artisans = Artisan.objects.all()
    total = artisans.count()

    par_ville = {}
    par_metier = {}
    for a in artisans:
        par_ville[a.ville] = par_ville.get(a.ville, 0) + 1
        par_metier[a.metier] = par_metier.get(a.metier, 0) + 1

    par_ville_sorted = sorted(par_ville.items(), key=lambda x: -x[1])
    par_metier_sorted = sorted(par_metier.items(), key=lambda x: -x[1])

    return render(request, 'artisans/dashboard.html', {
        'total': total,
        'nb_villes': len(par_ville),
        'nb_metiers': len(par_metier),
        'par_ville': par_ville_sorted,
        'par_metier': par_metier_sorted,
        'par_ville_json': json.dumps(par_ville_sorted),
        'par_metier_json': json.dumps(par_metier_sorted),
    })


# ─── Nouveau artisan ──────────────────────────────────────────────────────────

def nouveau(request):
    questions = Question.objects.filter(active=True)

    if request.method == 'POST':
        contact = request.POST.get('contact', '').strip()
        ville_choice = request.POST.get('ville', '').strip()
        metier_choice = request.POST.get('metier', '').strip()
        ville = request.POST.get('ville_autre', '').strip() if ville_choice == 'Autre' else ville_choice
        metier = request.POST.get('metier_autre', '').strip() if metier_choice == 'Autre' else metier_choice

        if not contact or not ville or not metier:
            messages.error(request, "Veuillez remplir tous les champs obligatoires.")
            return render(request, 'artisans/nouveau.html', {
                'questions': questions,
                'villes': VILLES,
                'metiers': METIERS,
                'post': request.POST,
                'ville_autre': request.POST.get('ville_autre', ''),
                'metier_autre': request.POST.get('metier_autre', ''),
            })

        artisan = Artisan.objects.create(contact=contact, ville=ville, metier=metier)

        for q in questions:
            contenu = request.POST.get(f'question_{q.id}', '')
            Reponse.objects.create(artisan=artisan, question=q, contenu=contenu)

        messages.success(request, f"Artisan #{artisan.id} enregistré avec succès !")
        return redirect('nouveau')

    return render(request, 'artisans/nouveau.html', {
        'questions': questions,
        'villes': VILLES,
        'metiers': METIERS,
        'post': {},
        'ville_autre': '',
        'metier_autre': '',
    })


# ─── Liste des réponses ───────────────────────────────────────────────────────

def reponses(request):
    qs = Artisan.objects.prefetch_related('reponses__question')
    search = request.GET.get('q', '').strip()
    ville_f = request.GET.get('ville', '')
    metier_f = request.GET.get('metier', '')

    if search:
        from django.db.models import Q
        qs = qs.filter(
            Q(contact__icontains=search) |
            Q(ville__icontains=search) |
            Q(metier__icontains=search)
        )
    if ville_f:
        qs = qs.filter(ville=ville_f)
    if metier_f:
        qs = qs.filter(metier=metier_f)

    artisan_detail = None
    detail_id = request.GET.get('detail')
    if detail_id:
        artisan_detail = get_object_or_404(
            Artisan.objects.prefetch_related('reponses__question'), pk=detail_id
        )

    villes_dispo = Artisan.objects.values_list('ville', flat=True).distinct()
    metiers_dispo = Artisan.objects.values_list('metier', flat=True).distinct()

    return render(request, 'artisans/reponses.html', {
        'artisans': qs,
        'artisan_detail': artisan_detail,
        'search': search,
        'ville_f': ville_f,
        'metier_f': metier_f,
        'villes_dispo': villes_dispo,
        'metiers_dispo': metiers_dispo,
        'total': qs.count(),
    })


# ─── Gestion des questions ────────────────────────────────────────────────────

def admin_questions(request):
    questions = Question.objects.prefetch_related('reponses__artisan').all()
    return render(request, 'artisans/questions.html', {'questions': questions})


@require_POST
def question_ajouter(request):
    texte = request.POST.get('texte', '').strip()
    if texte:
        max_ordre = Question.objects.count()
        Question.objects.create(texte=texte, ordre=max_ordre + 1, active=True)
        messages.success(request, "Question ajoutée.")
    return redirect('admin_questions')


@require_POST
def question_modifier(request, pk):
    q = get_object_or_404(Question, pk=pk)
    texte = request.POST.get('texte', '').strip()
    if texte:
        q.texte = texte
        q.save()
        messages.success(request, "Question mise à jour.")
    return redirect('admin_questions')


@require_POST
def question_toggle(request, pk):
    q = get_object_or_404(Question, pk=pk)
    q.active = not q.active
    q.save()
    return redirect('admin_questions')


@require_POST
def question_supprimer(request, pk):
    q = get_object_or_404(Question, pk=pk)
    q.delete()
    messages.success(request, "Question supprimée.")
    return redirect('admin_questions')


@require_POST
def question_monter(request, pk):
    q = get_object_or_404(Question, pk=pk)
    precedente = Question.objects.filter(ordre__lt=q.ordre).order_by('-ordre').first()
    if precedente:
        q.ordre, precedente.ordre = precedente.ordre, q.ordre
        q.save()
        precedente.save()
    return redirect('admin_questions')


@require_POST
def question_descendre(request, pk):
    q = get_object_or_404(Question, pk=pk)
    suivante = Question.objects.filter(ordre__gt=q.ordre).order_by('ordre').first()
    if suivante:
        q.ordre, suivante.ordre = suivante.ordre, q.ordre
        q.save()
        suivante.save()
    return redirect('admin_questions')


# ─── Export ───────────────────────────────────────────────────────────────────

def export_json(request):
    artisans = Artisan.objects.prefetch_related('reponses__question').all()
    data = []
    for a in artisans:
        data.append({
            'id': a.id,
            'contact': a.contact,
            'ville': a.ville,
            'metier': a.metier,
            'created_at': a.created_at.isoformat(),
            'reponses': [
                {'question': r.question.texte, 'reponse': r.contenu}
                for r in a.reponses.all().order_by('question__ordre')
            ],
        })
    response = HttpResponse(
        json.dumps(data, ensure_ascii=False, indent=2),
        content_type='application/json'
    )
    response['Content-Disposition'] = 'attachment; filename="artisans_etude.json"'
    return response


def export_csv(request):
    questions = Question.objects.filter(active=True).order_by('ordre')
    response = HttpResponse(content_type='text/csv; charset=utf-8')
    response['Content-Disposition'] = 'attachment; filename="artisans_etude.csv"'
    response.write('\ufeff')  # BOM pour Excel

    writer = csv.writer(response)
    headers = ['ID', 'Contact', 'Ville', 'Métier', 'Date']
    for q in questions:
        headers.append(f"Q{q.ordre}: {q.texte[:50]}")
    writer.writerow(headers)

    for a in Artisan.objects.prefetch_related('reponses__question').all():
        rmap = {r.question_id: r.contenu for r in a.reponses.all()}
        row = [a.id, a.contact, a.ville, a.metier,
               a.created_at.strftime('%d/%m/%Y %H:%M')]
        for q in questions:
            row.append(rmap.get(q.id, ''))
        writer.writerow(row)

    return response
