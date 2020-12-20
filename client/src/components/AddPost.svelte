<style lang="scss">
	section {
		padding-top: 0.5em;
	}
	
	#state {
		position: absolute;
		top: 0;
		right: 0;
		opacity: 0.33;
		font-size: 0.8em;
	}
	i {
    font-family: 'untitled-font-1';
}

.box {
    width: 40%;
    float: left;
    background: #15171b;
    padding: .5rem 1.5rem;
    margin: 10px 10px 5px 0;
    box-shadow: inset 0 0 4px  rgba(#000000, 0.8    );
    border-radius: 5px;
    transition: all .15s ease-in-out;
    text-align: center;
    opacity: .5;
    .icon {
        
    }
    .label {
        font-weight: bold;
        text-transform: uppercase;
        font-size: 0.7rem;
        opacity: .5;

    }
    
    &:hover {
        opacity: 1;
        box-shadow: inset 0 0 3px  rgba(#000000, 0.6    );

    }
}
</style>

<script>
  import { getContext } from 'svelte';
	import { fly } from 'svelte/transition';
	
	import PostDialog from './ClassDialog.svelte';
	import CloseButton from './CloseButton.svelte';

  const { open } = getContext('simple-modal');
	
	let opening = false;
	let opened = false;
	let closing = false;
	let closed = false;

	export let link, icon, label;
  
	let post_text;
	let status = 0;
	
	const onCancel = (text) => {
		name = '';
		status = -1;
	}
	
	const onOkay = (text) => {
		post_text = text;
		console.log(text)
		status = 1;
	}

  const showDialog = () => {
		open(
			PostDialog,
			{
				message: "Enter Post Details",
				hasForm: true,
				onCancel,
				onOkay
			},
			{
				closeButton: true,
    			closeOnEsc: false,
    			closeOnOuterClick: false,
			}
	  );
	};
</script>

<div class="box" on:click={showDialog}>
    <div class="icon">
        <i class="icon-{icon}"></i>
    </div>
    <div class="label">
        {label}
    </div>
</div>
