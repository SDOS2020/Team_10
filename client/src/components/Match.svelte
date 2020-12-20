
<style lang="scss">
    .style-one {
        background: rgb(15,16,19);
        background: linear-gradient(90deg, rgba(21,23,27,1) 0%, rgba(15,16,19,1) 50%, rgba(21,23,27,1) 100%);
    }
    .style-two {
        background: rgb(15,16,19);
        background: linear-gradient(45deg, rgba(21,23,27,1) 0%, rgba(15,16,19,1) 20%, rgba(21,23,27,1) 100%);
    }
    .style-three {
        background: rgb(15,16,19);
        background: linear-gradient(90deg, #15171b 0%, #0f1013 70%, #15171b 100%);
    }
    .card {
        padding: 1.5rem 1rem 3rem 1rem;
        border-radius: 10px;
        box-shadow: 0 0 5px rgba(#000,.4);
        margin-bottom: 10px;
        width: 95%;
        position: relative;
        top: 0px;
        transition: all .2s ease-in-out;

       
        align-items: center;
    }

    .card:hover {
        top: -3px;
        box-shadow: 0 3px 5px rgba(#000, .5);
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
        opacity: 1;
        font-size: 2rem;
    }

    .data {
        opacity: 1;
        font-size: 1rem;
    }

    .choose {
        /*position:relative;
        left: 70%;
        margin-top:50%;*/
        position: absolute;
        bottom: 5px;
        right: 5px;
    }

    .choose2 {
        /*position:relative;
        left: 70%;
        margin-top:50%;*/
        position: absolute;
        bottom: 5px;
        left: 5px;
    }


    
</style>    

<script>
    export let first_name = "John", last_name = "Doe", time = 0, qualification = "PhD", organization = "IIITD", areas = "ML, DL", styleNumber, id;
</script>

<a href="/">
    <section class="card style-{styleNumber}">
        <h1>Mentor</h1>
        <span class="title">{first_name} {last_name}</span>
        <span class="data"><br>
            Qualification: {qualification}<br>
            Organization: {organization}<br>
            Areas of Expertise: {areas}<br>
            Time Available for Mentoring: {time} hrs/week<br>
        <a class = "button button-secondary choose2" href = "/">Join Class</a> 

        <a class = "button button-secondary choose" href = "/">APPLY FOR Mentor</a> 
    </section>
</a>