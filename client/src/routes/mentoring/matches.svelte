<style lang="scss">

h1{
	font-size: 2rem;
	text-transform: uppercase; 
}
p {
    margin: 10px 0;
	opacity: .7;
}

form {

    display: inline-flex;
    // flex-direction: row;
}

form>* {
    margin: 10px 5px 10px 0;
}




.sub {
    font-size: 1rem;
    opacity: .8;
    margin-bottom: 20px; 

}

.badges {
    float: left;
    width: 100%;
    margin-bottom: 1em;
}
.badge {
    font-size: .6rem;
    text-transform: uppercase;
    padding:3px 10px;
    border-radius: 50px;
    color: #fff;
    display: inline-block;

}

.qualification {
    background: lighten(#467E84, 5%);
}

.user_type {
    background: #73645D;
}

</style>

<svelte:head>
	<title>Profile</title>
</svelte:head>

<script context="module">
    import { authCheck } from '../../utils/user';
    export async function preload(page, session) {
        // authCheck(session, this.redirect);
        const res = await this.fetch(`profileDetails/`);
        const userDetails = await res.json();
        return { userDetails };
    }
</script>  
<script>
    import Match from '../../components/Match.svelte';
    import ThreeColumn from '../../components/ThreeColumn.svelte';
    
    export let userDetails;
    console.log(userDetails)
</script>

    <ThreeColumn>
        
        <!-- <div slot="left">
            <Match first_name={userDetails[0].first_name} last_name={userDetails[0].last_name} time={userDetails[0].duration} qualification={userDetails[0].qualification} organization={userDetails[0].organization} areas={userDetails[0].requirements} styleNumber="two" ind=0/>
            </div>
        <div slot="middle">
            <Match first_name={userDetails[1].first_name} last_name={userDetails[1].last_name} time={userDetails[1].duration} qualification={userDetails[1].qualification} organization={userDetails[1].organization} areas={userDetails[1].requirements} styleNumber="two" ind=1/>        	
        </div>
        <div slot="right">
            <Match first_name={userDetails[2].first_name} last_name={userDetails[2].last_name} time={userDetails[2].duration} qualification={userDetails[2].qualification} organization={userDetails[2].organization} areas={userDetails[2].requirements} styleNumber="two" ind=2/>		
        </div> -->
    </ThreeColumn>