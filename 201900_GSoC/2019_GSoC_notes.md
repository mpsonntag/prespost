# GSoC notes

- Share evaluation text with student
- After evaluation ask student what can be improved
- Always tell the student when someone is not available
- Come up with a strategic plan for the project
    - which step at which point in time
- Deliver feedback early; Let them know right away what you think about their work.
- Make a point to give positive feedback: When a student completes a task on time, 
  and especially when they exceed your expectations, let them know!
- Don’t avoid critique, but phrase suggestions positively. Deliver personal critisism in a private forum.
  When in doubt, ask for advice from more experienced mentors or from your organization’s administrator.
- If we don't hear anything from the student for two days during the coding period, ask!

Project outline from the mentors side
-> check how this converges with the students project outline
-> Create issues and milestones on github to check that we are on track?

Preparations during bonding period
- Set up local gogs
- Set up gin valid
- Read into DroneCI
   - how do builds work
   - build file
   - where are results of a build stored
Coding start
- give a brief introduction to DroneCI & what has been discovered above
- from now on use the README.md to document
  all steps how to set up any of the involved services.
- set up an instance of DroneCI
- hook up DroneCI with local gogs
- clone a hooked repository
- dockerize DroneCI (if it is not already)
- update the DroneCI container to include everything required to run SnakeMake
- use provided data and snakemake file to run a snakemake build

other deliverables
- build queue - make sure only the latest version of a repo is built
- how can we make the results of a build available
  - list all options
    - push to original repo
    - make a PR with the results towards the original repo
    - have a DL page where the latest results can be found
- how can we efficiently store and reuse previous runs of snakemake and 
  rebuild only the necessary

