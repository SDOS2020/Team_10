## User model

mentor chooses mentee_list

- Mentor
    - first_name, last_name, email, ...
    - qualification (BTech, PhD, MS)
    - institution/industry (~)
    - requirement (field of study/mentorship)
    - classes[]
    - duration
    - interests ; give standard tech interests
    - isAnonymous

- Mentee
    - first_name, last_name, email, ...
    - qualification (year of study) : (currently I,II,III,IV)
    - college name
    - requirement (field of study/mentorship) : where he needs help : 
    - classes[]
    - interests ; give standard tech interests
    - isAnonymous
- study_groups
    - mentee_list []
    - shared knowledge_base
    - github link to project

- class 
    - newsfeed (posts + comments)
    - resources
    - projects -> github API (commits, open PRs, issues)
    - grading calculation (custom calculation)

- project
    - type: textual/code


- login/signup 
    - profile_details 
        - (mentor-mentee matching) 
            - homepage (matches, concise details on groups)

- classes
    - (list of students, mentor, projects(project tracking, comments), updates)

- knowledge_base
    - organized according to field of studies


TODO: 
- ask for initial requirements
- 