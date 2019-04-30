// Only HTML 5
document.getElementById('MyID').classList.add('MyClass');
document.getElementById('MyID').classList.remove('MyClass');
document.getElementById('MyID').classList.toggle('MyClass');

// jQuery
$('#MyElement').addClass('MyClass');
$('#MyElement').removeClass('MyClass');
if($('#MyElement').hasClass('MyClass')) {}
$('#MyElement').toggleClass('MyClass');

// plain JavaScript
document.getElementById("MyElement").className = "MyClass1 MyClass2 MyClass3";