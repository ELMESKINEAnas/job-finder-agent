from src.extractor import extract_job_offer

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

result = extract_job_offer(sample_offer)
print(result)