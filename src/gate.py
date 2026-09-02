REQUIRED={'multicloud': ['cloud_placement_policy', 'cloud_specific_modules', 'portable_platform_contract', 'region_metadata', 'data_residency', 'cost_model', 'blast_radius_boundaries', 'dependency_mapping'], 'kubernetes': ['requests_limits', 'health_probes', 'pdb', 'topology_spread', 'scaling_strategy', 'workload_identity', 'network_policy', 'immutable_images', 'graceful_shutdown', 'owner_slo'], 'linkerd': ['mtls', 'service_identity', 'telemetry', 'authorization_policy', 'proxy_coverage', 'certificate_monitoring', 'control_plane_health', 'overhead_monitoring'], 'gitops': ['argocd', 'git_source_of_truth', 'applicationsets', 'cluster_labels', 'staged_rollout', 'drift_reconciliation', 'rollback', 'deployment_audit'], 'iac': ['terraform', 'remote_state', 'locking', 'reviewed_plan', 'provider_modules', 'encryption_defaults', 'ownership_tags', 'backup_controls', 'drift_detection'], 'observability': ['metrics', 'logs', 'traces', 'deployment_events', 'mesh_metrics', 'cluster_capacity', 'cloud_dependency_health', 'cost_signals', 'slos', 'alert_owner'], 'reliability': ['zone_failure', 'cluster_failure', 'region_failure', 'cloud_failure', 'shared_control_plane_review', 'dns_failure', 'identity_failure', 'restore_test'], 'cicd': ['immutable_artifact', 'test_gate', 'security_scan', 'iac_validation', 'health_gate', 'progressive_delivery', 'rollback', 'artifact_provenance']}

def evaluate(spec):
 findings=[]
 for section,fields in REQUIRED.items():
  values=spec.get(section,{})
  for field in fields:
   if not values.get(field): findings.append(f"{section}.{field} is required")
 return {"allowed":not findings,"findings":findings}
