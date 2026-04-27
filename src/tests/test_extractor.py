from src.extractor import extract_job_offer
import pytest   

sample_offer = """ 
Offre de Stage : Ingénieur en IA Agente (H/F)

Entreprise : NexaCore Solutions (Startup spécialisée en automatisation intelligente)

Poste : Développeur Backend / IA

Ville : Lyon (69007) — Télétravail partiel possible

Description : Nous recherchons un(e) étudiant(e) passionné(e) pour concevoir et déployer des agents autonomes capables d'interagir avec des API tierces. Sous la supervision de notre CTO, vous travaillerez sur l'orchestration de workflows complexes.

Compétences demandées : * Maîtrise de Python et des frameworks d'orchestration (ex: LangGraph ou CrewAI).

Expérience avec les bases de données vectorielles (ChromaDB ou Qdrant).

Solides bases en conception d'APIs (FastAPI ou Node.js).

Conditions : * Durée : 6 mois (début Septembre 2026).

Rémunération : 1 250 € brut/mois + Tickets restaurants + 50% abonnement transports. 
"""

testing_with_another_sample_offer = """

Offre de Stage : Ingénieur en IA Agente (H/F)

Entreprise : NexaCore Solutions (Startup spécialisée en automatisation intelligente)

Poste : Développeur Backend / IA

Ville : Lyon (69007) — Télétravail partiel possible

Description : Nous recherchons un(e) étudiant(e) passionné(e) pour concevoir et déployer des agents autonomes capables d'interagir avec des API tierces. Sous la supervision de notre CTO, vous travaillerez sur l'orchestration de workflows complexes.

Compétences demandées : * Maîtrise de Python et des frameworks d'orchestration (ex: LangGraph ou CrewAI).

Expérience avec les bases de données vectorielles (ChromaDB ou Qdrant).

Solides bases en conception d'APIs (FastAPI ou Node.js).

Conditions : * Durée : 6 mois (début Septembre 2026).

"""

# result = extract_job_offer(sample_offer)
# print(result)


def test_empty_text():
    with pytest.raises(ValueError):
        extract_job_offer("")

def test_missing_fields() :
    result = extract_job_offer(testing_with_another_sample_offer)
    assert result.company == "NexaCore Solutions"
    assert result.title == "Ingénieur en IA Agente (H/F)"
    assert len(result.required_skills) > 0
    assert result.contract_type.lower().strip() == "internship"
    assert result.salary is None
    assert result.source_url is None
    assert result.posted_date is None

def test_irrelevent_text ():
    result = extract_job_offer("Bonjour je m'appelle Anas")
    assert result.company == ""
    assert result.title == ""
    assert len(result.required_skills) == 0

def test_fake_job_discussion():
    text = "I saw that Google was hiring last year, but I think they stopped."
    result = extract_job_offer(text)
    
    assert result.company == ""