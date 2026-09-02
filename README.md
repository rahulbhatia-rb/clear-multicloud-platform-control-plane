# Clear Multi-Cloud Platform Control Plane

Independent proof-of-work inspired by Clear / ClearTax's public infrastructure hiring context.

This project models a platform spanning AWS, GCP and OCI with Kubernetes, Linkerd, ArgoCD, Terraform, CI/CD and observability. The key design principle is a portable operational contract with provider-specific implementations where justified by cost, reliability, geography or customer requirements.

> Based only on publicly shared role context. It does not represent Clear's private architecture.

## Core problem
Design infrastructure for the system, not one service: choose cloud/region, contain blast radius, preserve portability without collapsing to a lowest-common-denominator platform, and keep the developer path consistent.

## Architecture
Developer -> CI -> ArgoCD -> EKS/GKE/OKE -> Linkerd -> workloads -> telemetry/SLOs/cost.

## Multi-cloud model
Standardize Kubernetes workload contracts, GitOps, Linkerd identity/mTLS, Terraform module interfaces, SLOs, security policy, ownership and observability. Allow provider-specific load balancers, IAM/workload identity, databases, object storage, KMS, DNS and egress.

## Placement decision
Evaluate reliability, cost, blast radius, data residency, customer cloud preference, latency, regional capacity and dependency concentration before selecting AWS/GCP/OCI.

## Kubernetes baseline
Requests/limits, probes, PDB, topology spread, autoscaling, workload identity, NetworkPolicy, immutable images, graceful shutdown, owner/SLO.

## Linkerd
Automatic mTLS, service identity, authorization policy and service telemetry. Also monitor control-plane health, proxy coverage, certificate lifecycle and proxy overhead.

## ArgoCD / GitOps
Git is desired state. Use ApplicationSets and cluster labels such as cloud, region, market, environment and criticality. Expand rollouts deliberately: canary cluster -> region -> cloud -> fleet.

## Terraform
Provider-specific modules behind common platform contracts. Avoid pretending EKS, GKE and OKE are identical. Standardize outputs and operational expectations instead.

## Observability
One logical telemetry contract across clouds: metrics, logs, traces, deployment events, mesh metrics, capacity, cloud dependency health, cost, SLOs and alert ownership.

## Failure domains
Pod, node, zone, cluster, region, cloud provider, GitOps control plane, observability, identity, DNS and data layer. A multi-cloud estate is not resilient if a single global dependency can fail all clouds.

## Geo expansion
1. Determine latency/residency/customer constraints. 2. Select cloud/region. 3. Terraform platform baseline. 4. Register cluster in ArgoCD. 5. Install Linkerd/telemetry. 6. Run conformance tests. 7. Canary workloads. 8. Test failure/restore. 9. Validate cost. 10. Gradually move traffic.

## Run locally
```bash
python -m unittest -v tests.test_gate
python src/cli.py examples/production.json
python src/cli.py examples/unsafe.json
```

## 30/60/90
0-30: map estate, portable vs provider-specific components, ArgoCD/Linkerd/observability baselines, failure/cost concentration.
31-60: production contract, Terraform modules, cluster onboarding, blast-radius controls, mesh/cross-cloud telemetry.
61-90: new-region automation, conformance testing, cloud-failure drills, placement cost optimization, lower developer cognitive load.
