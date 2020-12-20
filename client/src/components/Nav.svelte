<style lang="scss">
@import url('https://fonts.googleapis.com/css2?family=Playfair+Display:ital@1&display=swap');
nav {
    position: fixed;
    top: 0;
    width: 100%;
    background: #15171B;
    box-shadow: 0 0 5px rgba(#000, .1);
    // left: 50%;
    // top: 80%;
    // transform: translateX(-50%);
    z-index: 1000;
    padding: 2rem 2rem;
    text-align: center;
    .logo {
        display: none;
        font: 1.2em 'Playfair Display';
        float: left;
    }
    ul {
        li {
            margin-right: 1rem;
            list-style-type: none;
            display: inline-block;
            a {
                font-size: .9rem;
                font-family: IBM Plex Sans;
                font-weight: bold;
                text-transform: uppercase;
                color: #D6CCC1;
                border-bottom: 2px solid rgba(#D6CCC1, 0);
                transition: all .35s;
                padding-bottom: 2px;
                &:hover {
                    color: #fff;
                    border-bottom: 2px solid rgba(#D6CCC1, .3);

                }
            }
        }
    }
}

li.dropdown {
  display: inline-block;
}

.dropdown-content {
  display: none;
  position: absolute;
  background-color: #15171B;
  min-width: 160px;
  box-shadow: 0px 8px 16px 0px rgba(0,0,0,0.2);
  z-index: 1;
}

.dropdown-content a {
  color: black;
  padding: 12px 16px;
  text-decoration: none;
  display: block;
  text-align: left;
  color: #D6CCC1;
}

.dropdown-content a:hover {background-color: #15171B;}

.dropdown:hover .dropdown-content {
  display: block;
}

</style>

<!-- <script context="module">
    import { authCheck } from '../../utils/user';
    export async function preload(page, session) {
        // authCheck(session, this.redirect);
        const res = await this.fetch(`classList/`);
        const classList = await res.json();
        return { classList };

    }
</script>  -->
<script>
    export let classList = [
        {
            name: "Class 1",
            link: "class"
        },
        {
            name: "Class 2",
            link: "class"
        },
        {
            name: "Class 3",
            link: "class"
        }
    ]
</script>

<nav>
<div class="logo">
    <a href="/">WebMentor</a>
</div>
<ul>
    <li><a href="/">Home</a></li>
    <li class="dropdown"><a class="dropbtn">Classes</a>
        <div class="dropdown-content">
    {#each classList as c}
      <a href={c.link}>{c.name}</a>
    {/each}
    </div>
    </li>
    <li><a href="/studybase">StudyBase</a></li>
    <li><a href="/profile">Profile</a></li>
    <li><a href="/logout">Logout</a></li>
</ul>
</nav>
