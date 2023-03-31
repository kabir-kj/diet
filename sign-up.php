<?php 
require('top.inc.php');
?>

    <!-- Header -->
    <header id="header" class="ex-2-header">
        <div class="container">
            <div class="row">
                <div class="col-lg-12">
                    <h1>Sign Up</h1>
                   <p>Fill out the form below to sign up for NutriGenie. Already signed up? Then just <a class="white" href="log-in.php">Log In</a></p> 
                    <!-- Sign Up Form -->
                    <div class="form-container">
                        <form id="signUpForm" data-toggle="validator" data-focus="false">
                            <div class="form-group">
                                <input type="email" class="form-control-input" id="semail" name ="email"required>
                                <label class="label-control" for="semail">Email</label>
                                <div class="help-block with-errors"></div>
                                <span class="field_error" id="email_error"></span>
                            </div>
                            <div class="form-group">
                                <input type="text" class="form-control-input" id="sname" name="name" required>
                                <label class="label-control" for="sname">Name</label>
                                <div class="help-block with-errors"></div>
                                <span class="field_error" id="name_error"></span>
                            </div>
                            <div class="form-group">
                                <input type="password" class="form-control-input" id="spassword" name="password" required>
                                <label class="label-control" for="spassword">Password</label>
                                <div class="help-block with-errors"></div>
                                <span class="field_error" id="password_error"></span>
                            </div>
                            <div class="form-group">
                                <button type="submit" class="form-control-submit-button" onclick="user_register()"  formaction="index.php">SIGN UP</button>
                            </div>
                            <div class="form-message">
                                <div id="smsgSubmit" class="h3 text-center hidden"></div>
                            </div>
                        </form>
                    </div> <!-- end of form container -->
                    <!-- end of sign up form -->

                </div> <!-- end of col -->
            </div> <!-- end of row -->
        </div> <!-- end of container -->
    </header> <!-- end of ex-header -->
    <!-- end of header -->


    <!-- Scripts -->
    <script>
        function user_register(){
	jQuery('.field_error').html('');
	var name=jQuery("#sname").val();
	var email=jQuery("#semail").val();
	var password=jQuery("#spassword").val();
	var is_error='';
	if(name==""){
		jQuery('#name_error').html('Please enter name');
		is_error='yes';
	}if(email==""){
		jQuery('#email_error').html('Please enter email');
		is_error='yes';
	}if(password==""){
		jQuery('#password_error').html('Please enter password');
		is_error='yes';
	}
	if(is_error==''){
		jQuery.ajax({
			url:'register_submit.php',
			type:'post',
			data:'name='+name+'&email='+email+'&password='+password,
			success:function(result){
				if(result=='email_present'){
					jQuery('#email_error').html('Email id already present');
				}
				if(result=='insert'){
					jQuery('.register_msg p').html('Thank you for registeration');
				}
			}	
		});
	}
	
}
        </script>


    <script src="js\jquery.min.js"></script> <!-- jQuery for Bootstrap's JavaScript plugins -->
    <script src="js\popper.min.js"></script> <!-- Popper tooltip library for Bootstrap -->
    <script src="js\bootstrap.min.js"></script> <!-- Bootstrap framework -->
    <script src="js\jquery.easing.min.js"></script> <!-- jQuery Easing for smooth scrolling between anchors -->
    <script src="js\swiper.min.js"></script> <!-- Swiper for image and text sliders -->
    <script src="js\jquery.magnific-popup.js"></script> <!-- Magnific Popup for lightboxes -->
    <script src="js\validator.min.js"></script> <!-- Validator.js - Bootstrap plugin that validates forms -->
    <script src="js\scripts.js"></script> <!-- Custom scripts -->
</body>
</html>