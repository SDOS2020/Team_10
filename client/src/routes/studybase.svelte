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
.action-mini_wrapper {

    width: 100%;
    // padding: 1rem;
    margin-top: 1rem;
}

:global([ref=childClass]) {
    background: #0F1013;
  }

</style>

<svelte:head>
	<title>Profile</title>
</svelte:head>

<!-- <script context="module">
    import { authCheck } from '../../utils/user';
    export async function preload(page, session) {
        // authCheck(session, this.redirect);
        const res = await this.fetch(`profileDetails/`);
        const postDetails = await res.json();
        return { postDetails };
    }
</script>   -->
<script>
    import Card from '../components/Card.svelte';
    import TwoColumn from '../components/TwoColumn.svelte';
    import ActionMini from '../components/ActionMini.svelte';
    import AddPost from '../components/AddPost.svelte'
    import Modal from '../components/Modal.svelte'
    import PopUpForm from '../components/PopUpForm.svelte'


    export let postDetails;
    
    console.log(postDetails)
</script>




    <TwoColumn>
        <div slot="left">

                    <Card title="Resources"  subtext="" link="Some text" styleNumber="one" ispost={false}/>
                   <div class="action-mini_wrapper">
                    <Modal>
                        <PopUpForm icon="folder-add" label="Create Project" />
                    </Modal>
                    <ActionMini link="" icon="book-read-streamline" label="Add Resources" />
                </div>
        </div>
        
<div ref = "childClass" slot="right">
            <!-- {#each postDetails as post} -->
                <Card title="Resource Name" subtext="Resource Description" link="" styleNumber="two" ispost={false} />
            <!-- {/each} -->
        </div>
    </TwoColumn>
        
<!-- instant announcement -->