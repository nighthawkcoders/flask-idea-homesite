#Data "setup" for Projects 
#next step would be to extract project data from a database
def setup():
  #Person Data
  name = "KILA Comedy"
  github = "https://github.com/iniyaam/Python-Web-Portfolio-Series-1"
  linkedin = "#"
  youtube = "#"
  twitter = "#"
  source = {"name": name, "github": github, "linkedin": linkedin, "youtube": youtube, "twitter": twitter}
  #Project Data
  project1 =  "History of Comedy"
  projlinks1 = [
    Link("Project Plan", "https://docs.google.com/document/d/1VelBBpneDJVcsaPZCT5Qb72xthwv9PCPSnQTGb2yWMA/edit"),
    Link("Repl", "https://repl.it/@Ryanshay18/ResponsibleFastDesignmethod?#README.md"),
    Link("Resources", "https://padlet.com/jmortensen7/csp2021")
  ]
  project2 =  "Comedians Through The Decades"
  projlinks2 = [
    Link("Project Plan",
    "https://docs.google.com/document/d/1T3cajl0kOPPRUfHDqBrKtmC6Ria0kW8E0_gJo3ur6vc/edit?usp=sharing"),
    Link("Repl", "https://repl.it/@jmort1021/Python-Web-Portfolio-Series?__cf_chl_jschl_tk__=cff72504752e89d50dea999ce10f859a17ecc294-1603026111-0-AdBP5FO-3nyUc_KVdPlNwvXM4MwUXy1HXHmbiJui1YBnUTPJZ8X4UBZVeYUXrnwRBJVvku9NftGYDWtp8lp4KovKX55R8S4twedzHpa2snwLwoAWaxuc4rgAa2l9J_rWqnNvUNcjJ8-p1V1RuTWV3lIy149lptozqAQdJnGj7PlcJxnu3YH22EXK-jl7bmdQmW9r_9fE1xp8J7sOFS3I1PMgmtoExcDIQSBBTnx1zQsyQGNS6wnuX72MAPnS_x3ZL1ETNRgFbVKpLsFJiR9ED1ErU54wyZYrUxEbZ_txHd7qY1T_s_lE6Ll8jYWHx-GulQ#main.py"),
    Link("Resources", "https://padlet.com/jmortensen7/csptime1_2")
  ]
  #Project Objects
  proj1 = Project(project1, projlinks1)
  proj2 = Project(project2, projlinks2)
  #HTML Data
  projects = Projects(source, [proj1, proj2])
  return projects

#Link class contains button (label) and hypertext reference (href)
class Link():
  #link data with button and href (url)
  def __init__(self, btn, href):
    self.btn = btn
    self.href = href
  def get_btn(self):
    return self.btn
  def get_href(self):
    return self.href

#Project data class contain project name and links (Link class objects)
class Project():
  #project data with name and links
  def __init__(self, name, links):
    self.name = name
    self.links = links
  def get_name(self):
    return self.name
  def get_links(self):
    return self.links

#Projects class contains person (owner) and multiple projects (Project class objects)
class Projects():
  #HTML data with source and projects    
  def __init__(self, source, projects):
    self.source = source
    self.projects = projects
  #source data getter
  def get_source(self):
    return self.source
  #project data getter
  def get_projects(self):
    return self.projects
