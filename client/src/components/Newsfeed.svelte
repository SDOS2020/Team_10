<style>
    .wrapper {
        height: 100%;
        width: 40%;
        position: fixed;
        z-index: 1;
        left: 40%;
        

 
    }

    

    .wrapper form input[type="text"] {
        width: 90%;
        height: 10vmin;
        margin-left: 5%;
        margin-right: 5%;
        margin-top: 2.5%;
        margin-bottom: 1.5%;
        display: block;
        padding: 10px 10px;
        border: 1px solid #999;
        border-radius: 5px;
        box-shadow: 1px 1px #888888;
        background: #fff;
        font-size: 14px;
        font-family: var(--font-default);
        letter-spacing: 1px;

        
        
    }

    .wrapper form input[type="submit"] {
         
        background: #333;
        border: none !important;
        outline: none !important;
        padding: 10px 10px;
        color: #fff;
        letter-spacing: 1px;
        cursor: pointer;
        border-radius: 5px;
        position: relative;
        margin-left: 5%;
        margin-right: 5%;
        width:90%;
        
    }



</style>

<div class="wrapper">
    <form>
        <input type="text" name="post" placeholder="Share something with the class!">        

        <input type="submit" value="POST">
    </form>




</div>