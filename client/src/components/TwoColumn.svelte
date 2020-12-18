<style lang="scss">
.main {
	position: relative;
    width: 70%;
	// left: 50%;
    // transform: translateX(-50%);
    margin: 0 auto;
}
@media screen and (max-width:1280px) {
    .main {
        width: 90%;
    }
}

.wrapper {
    position: relative;
    top: 10vmin;
	border-radius: 5px;
	// box-shadow: 0 0 6px rgba(#000, 0.07);
	padding: 2rem 0rem 2rem 2rem;

}
.left {
    float: left;
    width: 25%;
}

.right {
    float: left;
    width: 75%;
    background: rgba(#15171b, 1);
    padding: 2rem 1rem;

}


@media screen and (max-width:780px) {
    .left, .right{
        float: none;
        width: 90%;
    }

    .left {
        width: 50%;
    }
}

</style>

<script>

</script>


<section class="main">
    <section class="wrapper">
        <div class="left">
            <slot name="left"></slot>
        </div>
        <div class="right">
            <slot name="right"></slot>
        </div>
    </section>
</section>