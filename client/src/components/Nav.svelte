<style lang="scss">
nav {
    position: fixed;
    width: 100%;
    background: #15171B;
    box-shadow: 0 0 5px rgba(#000, .1);
    left: 50%;
    // top: 80%;
    transform: translateX(-50%);
    z-index: 1000;
    padding: 2rem 2rem;

    ul {
        float: right;
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
</style>

<nav>
<ul>
    <li><a href="/">Home</a></li>
    <li><a href="/classes">Classes</a></li>
    <li><a href="/knowledge">StudyBase</a></li>
    <li><a href="/profile">Profile</a></li>
    <li><a href="/logout">Logout</a></li>
</ul>
</nav>
