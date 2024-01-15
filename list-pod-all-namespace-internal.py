from kubernetes import client,config
#config.load_kube_config()
config.load_incluster_config()
v1 = client.CoreV1Api()

print("list pods in all namespaces")

k = v1.list_pod_for_all_namespaces(watch=False)

for i in k.items:
    print(i.metadata.namespace,"    ",i.metadata.name)
