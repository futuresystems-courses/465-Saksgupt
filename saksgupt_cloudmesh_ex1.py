import cloudmesh
mesh = cloudmesh.mesh("mongo")
username = cloudmesh.load().username()
mesh.activate(username)
mesh.vmname()
print cloudmesh.version()
