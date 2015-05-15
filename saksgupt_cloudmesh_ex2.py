import cloudmesh
from pprint import pprint

mesh = cloudmesh.mesh("mongo")
username = cloudmesh.load().username()
print username
mesh.activate(username)
print cloudmesh.shell("cloud on india")
print cloudmesh.shell("cloud list")
