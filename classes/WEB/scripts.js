$(document).ready(function(){
    
    $("#salvar").click(function() { 

        var salvou = true;

        if(!($("#nome").val())) {
            $("#nome").css("border-color", "#FA5858");
            $("#nome").css("color", "#FA5858");
            salvou = false;
        } else {
            $("#nome").css("border-color", "#CCC");
            $("#nome").css("color", "black");
        }

        if(!($("#sobrenome").val())) {
            $("#sobrenome").css("border-color", "#FA5858");
            $("#sobrenome").css("color", "#FA5858");
            salvou = false;
        } else {
            $("#sobrenome").css("border-color", "#CCC");
            $("#sobrenome").css("color", "black");
        }

        if(!($("#email").val())) {
            $("#email").css("border-color", "#FA5858");
            $("#email").css("color", "#FA5858");
            salvou = false;
        } else {
            $("#email").css("border-color", "#CCC");
            $("#email").css("color", "black");
        }

        if(!($("#matricula").val())) {
            $("#matricula").css("border-color", "#FA5858");
            $("#matricula").css("color", "#FA5858");
            salvou = false;
        } else {
            $("#matricula").css("border-color", "#CCC");
            $("#matricula").css("color", "black");
        }

        if(!($("#usuario").val())) {
            $("#usuario").css("border-color", "#FA5858");
            $("#usuario").css("color", "#FA5858");
            salvou = false;
        } else {
            $("#usuario").css("border-color", "#CCC");
            $("#usuario").css("color", "black");
        }

        if(!($("#senha").val())) {
            $("#senha").css("border-color", "#FA5858");
            $("#senha").css("color", "#FA5858");
            salvou = false;
        } else {
            $("#senha").css("border-color", "#CCC");
            $("#senha").css("color", "black");
        }

        if(!($("#confirma-senha").val())) {
            $("#confirma-senha").css("border-color", "#FA5858");
            $("#confirma-senha").css("color", "#FA5858");
            salvou = false;
        } else {
            $("#confirma-senha").css("border-color", "#CCC");
            $("#confirma-senha").css("color", "black");
        }

        var senha1 = $("#senha").val();
        var senha2 = $("#confirma-senha").val();
        if(senha1 !== senha2) {
            $("#senha").css("border-color", "#FA5858");
            $("#confirma-senha").css("border-color", "#FA5858");
            alert("Senhas diferentes!");
        }

        if(salvou) {
            $(".campo").val("");
            $("#nome").focus();
        }
    });

});