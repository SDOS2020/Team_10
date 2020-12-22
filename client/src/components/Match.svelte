
<style lang="scss">
    .card {
        pwadding: 1.5rem 1rem 3rem 1rem;
        border-radius: 10px;
        margin-bottom: 10px;
        background: #15171b;
        width: 95%;
        min-height: 50%;
        position: relative;
        top: 0px;
        transition: all .2s ease-in-out;

        align-items: center;
    }

    h1 {
        opacity: .8;
    }
    h3 {
        font-size: .8rem;
        text-transform: uppercase;
        opacity: .6;
        font-weight: normal;
    }
    .title {
        opacity: .8;
        font-size: 1.5rem;
        text-transform: uppercase;
    }

    .data {
        opacity: 1;
        font-size: 1rem;

        ul {
            margin: 0 0 10px 0;
            padding: 10px 0; 
            li {
                font-size: .8rem;

                list-style-type: none;
                .label {
                    text-transform: uppercase;
                    opacity: .8;
                    font-size: .7rem;
                }
            }
        }

    }




    
</style>    

<script>
    export let first_name = "John", last_name = "Doe", time = 0, qualification = "PhD", organization = "IIITD", areas = "ML, DL", styleNumber, id;
</script>

<a href="/">
    <section class="card style-{styleNumber}">
        <h1>Mentor</h1>
        <h2 class="title">{first_name} {last_name}</h2>
        <div class="data">
            <ul>
                <li><span class="label">Qualification:</span> {qualification}</li>
                <li><span class="label">Organization: </span>{organization}</li>
                <li><span class="label">Areas of Expertise: </span>{areas}</li>
                <li><span class="label">Time Available for Mentoring:</span> {time} hrs/week</li>
            </ul>
            
            
            
            
        <a class = "button button-secondary choose2" href = "/">Apply for mentoring</a> 
        <a class = "button button-secondary choose1" href = "/">View Mentor</a> 

    </section>
</a>