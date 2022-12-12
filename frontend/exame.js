$(function() {
    
    // código para mapear click do botão incluir cedula
    $(document).on("click", "#btAddExame", function() {
        //pegar dados da tela
        nome = $("#nomeExameCard").val();
        descricao = $("#descricaoExameCard").val();
        resultado = $("#resultadoExameCard").val();
        paciente = $("#pacienteExameCard").val();
        medico = $("#medicoExameCard").val();
        doenca = $("#doencaExameCard").val();
        hospital = $("#hospitalExameCard").val();


        // preparar dados no formato json
        var dados = JSON.stringify({ nome: nome, descricao: descricao, resultado: resultado, paciente: paciente, medico: medico, doenca: doenca, hospital: hospital});
        // fazer requisição para o back-end
        $.ajax({
            url: 'http://localhost:5000/exame',
            type: 'POST',
            dataType: 'json', // os dados são recebidos no formato json
            contentType: 'application/json', // tipo dos dados enviados
            data: dados, // estes são os dados enviados
            success: exameIncluido, // chama a função listar para processar o resultado
            error: erroAoIncluir
        });
        function exameIncluido (retorno) {
            if (retorno.resultado == "ok") { // a operação deu certo?
                // informar resultado de sucesso
                alert("exame incluído com sucesso!");
                window.location.reload();

            } else {
                // informar mensagem de erro
                alert("Erro ao incluir exame");
            }            
        }
        function erroAoIncluir (retorno) {
            // informar mensagem de erro
            alert("Erro ao contactar back-end");
        }
    });
});