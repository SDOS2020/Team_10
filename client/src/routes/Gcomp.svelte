<script>
	export let text = "Project Details";
	export let grade = "P";
</script>

<style>
	p.double {border-style: double;}
	* {
  box-sizing: border-box;
	}

	/* Create two unequal columns that floats next to each other */
	.column {
	  float: left;
	  padding: 10px;
	}

	.left {
	  width: 80%;
	}

	.right {
	  width: 20%;
	}

	/* Clear floats after the columns */
	.row:after {
	  content: "";
	  display: table;
	  clear: both;
	}
	
</style>
<div class="row">
  <div class="column left">
    <p class = "double">{text}</p>
  </div>
  <div class="column right">
    <p class = "double">{grade}</p>
  </div>
</div>
