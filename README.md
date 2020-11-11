# WebMP: Web Mentoring Platform

Source code for WebMP, the proposed web mentoring platform. The code is divided into two directories, `client` and `server`.

## Instructions
Follow sequentially on first run.

- Clone repository, navigate to `client/`.
- Run `npm install` followed by a `npm run dev`
- Navigate to `server/`, run `pipenv shell` followed by a `pipenv install` to set up the python virtual environment.

- Set up PostgreSQL:
    - Install PostgreSQL 12.
    - Switch to user postgres using `sudo -u postgres -i`
    - Enter interactive mode using `psql`
    - Set password such like: `\password postgres` &lt;set password&gt;
    - Add the set password to path through your shell's `.rc` file (bashrc, zshrc, etc), under the name `DB_PASSWD`.
    - Navigate to `server/`, run `python3 manage.py makemigrations` followed by a `python3 manage.py migrate` to populate the database.
- Run backend server using, `python3 manage.py runserver`.

Navigate to [http://localhost:3000](http://localhost:3000) to view the Svelte client.

## Contributing Guidelines
- Checkout to your branch using `git checkout <first_name>`, do with `-b` flag, if branch not already created.
- Pull from master, using `git fetch origin master` followed by a `git merge`.
- **ONLY** open pull requests for code which is critical to the master repository. Divide every goal into features, and open PRs in terms of feature completion. For ex: `PR#1 : [Feature] Created signup form component`
- Commit messages follow the following format &lt;`[client/server] commit description`&gt; (ex: `[server] Registration input sanitization`)
- Lint the files before pushing, use `npm run lint`, to run ESLint on all `.svelte, js` files. As a convention, spacing is done in 4 spaces.
- CSS is written in SCSS, a pre-processed language. HTML classes/ids will follow the BEM structure of naming.


Individual READMEs for common bugs, will be present in both the `client/` and `server/` directories.


