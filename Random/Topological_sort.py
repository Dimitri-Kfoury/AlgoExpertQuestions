def topologicalSort(jobs, deps):
    graph = Graph(jobs, deps)

    orderedJobs = []
    jobsWithNoPre = []
    for job in graph.jobs.values():
        if job.number_of_pre == 0:
            jobsWithNoPre.append(job)

    while len(jobsWithNoPre):
        job = jobsWithNoPre.pop()
        orderedJobs.append(job.job)
        updateNumber(job, jobsWithNoPre)
    hasEdges = any(job.number_of_pre for job in graph.jobs.values())
    return [] if hasEdges else orderedJobs


class Graph:
    def __init__(self, jobs, deps):
        self.jobs = {}
        for job in jobs:
            self.jobs[job] = Node(job)
        for job, dep in deps:
            self.getNode(job).addDependency(self.getNode(dep))

    def getNode(self, job):
        if job not in self.jobs:
            self.jobs[job] = Node(job)
        return self.jobs[job]


class Node:
    def __init__(self, job):
        self.job = job
        self.deps = []
        self.number_of_pre = 0

    def addDependency(self, dep):
        self.deps.append(dep)
        dep.number_of_pre += 1


def updateNumber(job, newJobs):
    while len(job.deps):
        dep = job.deps.pop()
        dep.number_of_pre -= 1
        if dep.number_of_pre == 0:
            newJobs.append(dep)


