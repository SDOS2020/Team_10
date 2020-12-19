<script>
  import { getContext } from 'svelte';
  export let message;
	export let hasForm = false;
	export let onCancel = () => {};
	export let onOkay = () => {};

  const { close } = getContext('simple-modal');
	
	let value;
	let post_text;
	let onChange = () => {};
	
	function _onCancel() {
		onCancel();
		close();
	}
	
	function _onOkay() {
		onOkay(post_text);
		close();
	}
	
	// $: onChange(project_name)
</script>

<style>
  h2 {
		font-size: 2rem;
		text-align: center;
		color: #D6CCC1;
	}
	
	input {
		width: 100%;
	}
	
	.buttons {
		display: flex;
		justify-content: space-between;
	}
	
	.close {
		position: absolute;
		top: -2rem;
		right: 0;
		background: black;
	}
	form {
    display: flex;
    flex-direction: column;
	}

	form>* {
	    margin: 10px;
	}

	form .input-border {
    padding: 10px 10px;
    border: 1px solid #999;
    background: #15171b;
    font-size: 14px;
    font-family: var(--font-default);
    letter-spacing: 1px;
}
</style>

<button class="close" on:click={_onCancel}>
	Close
</button>

<h2>{message}</h2>

{#if hasForm}
	<!-- <input
    type="text"
	  bind:value
	  on:keydown={e => e.which === 13 && _onOkay()} /> -->
	  <form action="" method="POST">  
		  <input type="PostText" bind:value={post_text} name="posttext" placeholder="Post Text" required class="input-border">
		  <div class="buttons">
		<button on:click={_onCancel}>
			Cancel
		</button>
		<button typpe = "submit" on:click={_onOkay}>
			Add
		</button>
		</div>
	</form>

{/if}

<!-- <div class="buttons">
	<button on:click={_onCancel}>
		Cancel
	</button>
	<button on:click={_onOkay}>
		Add
	</button>
</div> -->