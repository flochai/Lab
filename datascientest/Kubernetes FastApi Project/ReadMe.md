# Project Summary

This project was created as part of my DataScientest DevOps course. The objective was to containerize, orchestrate, and expose a FastAPI application connected to a PostgreSQL database using Kubernetes.

## Tech Stack

- FastAPI — REST API with basic CRUD for users
- PostgreSQL — managed via Kubernetes StatefulSet
- Kubernetes (K3s) — lightweight K8s distribution deployed on Raspberry Pi 4 cluster
- Docker — containerized the full stack
- Cloudflare (planned) — for future tunnel setup and external secure access
- Macbook SSH access — for remote cluster management

## Kubernetes Deployment

**Namespace:** `standard`

### PostgreSQL:

- StatefulSet with persistent storage
- Secret for database credentials
- ConfigMap for non-sensitive configuration

### FastAPI:

- Deployment with 3 replicas
- Exposed via ClusterIP service

### Ingress Controller:

- Traefik Ingress to route external HTTP traffic

## Additional Context

- YAML manifests located in the `YAML-STANDARD` directory.
- Built custom Docker image for FastAPI using `docker buildx` to support ARM architecture of Raspberry Pi.
- Successfully troubleshooted various common Kubernetes challenges:
  - PVC binding issues
  - DNS resolution in-cluster and externally
  - ARM/AMD image compatibility
  - Ingress accessibility

---

## Feelings & Difficulties

This project allowed me to face many real-world DevOps challenges, especially when working directly on bare-metal hardware (Raspberry Pi) with ARM architecture.

- Had to deal with multi-architecture Docker builds (`docker buildx`) to ensure compatibility between my MacBook (ARM) and the Pi.
- Encountered persistent volume claim issues with StatefulSets and PVC binding delays due to `WaitForFirstConsumer` mode.
- Spent time troubleshooting DNS resolution issues inside and outside the cluster, especially around Ingress and external access.
- Learned how networking differs between local devices, cloud, and cluster-internal resources.
- Gained hands-on experience with Kubernetes troubleshooting tools: `kubectl describe`, `kubectl logs`, `k9s`, and others.
- Deployed, tested, broke things, fixed them again — multiple times. 😄

Despite the difficulties, I really enjoyed the iterative problem-solving process. This project gave me practical confidence with Kubernetes, YAML, Docker, Ingress, Services, Persistent Volumes, and cluster management — skills highly relevant for real-world DevOps work.

---

## Planned Next Steps

- Deploy Cloudflare Tunnel to securely expose services to the public internet without exposing my home IP.
- Automate deployments with Helm or Kustomize.
- CI/CD integration for automated builds & deployments.




---


# Résumé du projet

Ce projet a été réalisé dans le cadre de ma formation DevOps chez DataScientest. L’objectif était de conteneuriser, orchestrer et exposer une application FastAPI connectée à une base de données PostgreSQL via Kubernetes.

## Stack Technique

- **FastAPI** — API REST avec des opérations CRUD basiques pour les utilisateurs
- **PostgreSQL** — géré via un StatefulSet Kubernetes
- **Kubernetes (K3s)** — distribution K8s légère déployée sur un cluster Raspberry Pi 4
- **Docker** — conteneurisation de l’ensemble de la stack
- **Cloudflare (prévu)** — pour la mise en place future d’un tunnel sécurisé et d’un accès externe
- **Accès SSH Macbook** — pour l'administration distante du cluster

## Déploiement Kubernetes

**Namespace :** `standard`

### PostgreSQL :

- StatefulSet avec stockage persistant
- Secret pour les identifiants de la base de données
- ConfigMap pour la configuration non sensible

### FastAPI :

- Deployment avec 3 réplicas
- Exposé via un service de type ClusterIP

### Ingress Controller :

- Ingress Traefik pour router le trafic HTTP externe

## Contexte additionnel

- Les fichiers YAML se trouvent dans le dossier `YAML-STANDARD`.
- Image Docker personnalisée construite pour FastAPI avec `docker buildx` afin de supporter l’architecture ARM du Raspberry Pi.
- Résolution de plusieurs problématiques courantes Kubernetes :
  - Problèmes de liaison des volumes persistants (PVC binding)
  - Résolution DNS interne et externe
  - Compatibilité des images ARM/AMD
  - Accessibilité via Ingress

---

## Ressenti & Difficultés

Ce projet m’a confronté à de nombreux défis concrets du monde DevOps, notamment en travaillant directement sur du hardware (Raspberry Pi) en architecture ARM.

- Gestion des builds multi-architecture avec `docker buildx` pour garantir la compatibilité entre mon MacBook (ARM) et le Raspberry Pi.
- Difficultés liées aux PersistentVolumeClaims (PVC) et aux délais de liaison à cause du mode `WaitForFirstConsumer`.
- Dépannage de nombreux problèmes de résolution DNS, aussi bien dans le cluster qu’en externe, notamment sur l’Ingress et l’accès public.
- Compréhension approfondie des différences réseau entre machines locales, cloud et ressources internes au cluster.
- Utilisation concrète des outils de troubleshooting Kubernetes : `kubectl describe`, `kubectl logs`, `k9s`, etc.
- J’ai déployé, testé, cassé, réparé… à plusieurs reprises. 😄

Malgré les difficultés, j’ai beaucoup apprécié le processus d’apprentissage itératif. Ce projet m’a permis de consolider mes compétences pratiques sur Kubernetes, YAML, Docker, Ingress, Services, Volumes persistants et gestion de cluster — des compétences essentielles pour le métier de DevOps.

---

## Prochaines étapes prévues

- Mettre en place un tunnel Cloudflare pour exposer les services de manière sécurisée sans exposer l’IP de mon réseau personnel.
- Automatiser les déploiements avec Helm ou Kustomize.
- Mettre en place une intégration CI/CD pour automatiser les builds et les déploiements.
