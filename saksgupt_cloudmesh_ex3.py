import cloudmesh
from pprint import pprint

mesh = cloudmesh.mesh("mongo")
username = cloudmesh.load().username()
print username
mesh.activate(username)
print cloudmesh.shell("cloud on india")
print cloudmesh.shell("cloud list")
flavor = mesh.flavor('india', 'm1.small')
image=mesh.image('india','futuresystems/ubuntu-14.04')
result = mesh.start("india", username)
pprint (result)
