function GithubRepo(username, reponame){
    var issues;
    var url = "https://api.github.com/repos/"+username+"/"+reponame+"/issues";
    var promisses = {
        async: {
            busca_issues_e_popula: function (id) {
                /*
                Faz uma requisicao asincrona e promete preencher a tabela
                */
                $(id).html("Buscando issues...");
                $.when($.get(url)).then(function (issues) {

                    $(id).html("<tr><th>Numero</th><th>Titulo</th>")
                    $.each(issues, function (idx, issue) {
                        $(id).append("<tr><td>"+issue.number+"</td><td>"+issue['title']+"</td></tr>")
                    })
                });
            },

            busca_issues: function (id) {
                /*
                Faz uma requisicao asincrona e preenche a variável do closure
                */
                $(id).html("Buscando issues...");
                $.when($.get(url)).then(function (result) {
                    issues = result
                });
            },

            popula_tabela: function(id) {
                /*
                Faz uma requisicao asincrona e checa, de segundo em segundo, se tem dados
                */

                var espera_issues = setInterval(function () {

                    if (issues != undefined) {
                        $(id).html("<tr><th>Numero</th><th>Titulo</th>")
                        $.each(issues, function (idx, issue) {
                            $(id).append("<tr><td>"+issue.number+"</td><td>"+issue['title']+"</td></tr>")
                        })
                        clearInterval(espera_issues)
                    }

                }, 1000)

                
            }
        },
        sync: {
            busca_issues: function (id) {
                /*
                Faz uma requisicao sincrona e preenche a variável do closure
                */
                $(id).html("Buscando issues...");
                $.ajax({
                    url: url,
                    async: false, // olha a lapada!
                    success: function (result) {
                        issues = result
                    }
                });
            },

            popula_tabela: function(id) {

                /*
                Faz uma requisicao sincrona e checa, de segundo em segundo, se tem dados
                */
                $(id).html("<tr><th>Numero</th><th>Titulo</th>")
                $.each(issues, function (idx, issue) {
                    $(id).append("<tr><td>"+issue.number+"</td><td>"+issue['title']+"</td></tr>")
                })
                
            }
        }
    }
    return promisses;
}


function buscarIssuesAsync() {
    
    var username = $("#user").val();
    var reponame = $("#reponame").val();
    var le_repo = GithubRepo(username, reponame);

    le_repo.async.busca_issues_e_popula("#issuestable");

}

function buscarIssuesAsyncInterval() {
    
    var username = $("#user").val();
    var reponame = $("#reponame").val();
    var le_repo = GithubRepo(username, reponame);

    le_repo.async.busca_issues("#issuestable");
    le_repo.async.popula_tabela("#issuestable");
    
}
function buscarIssuesSync() {
    
    var username = $("#user").val();
    var reponame = $("#reponame").val();
    var le_repo = GithubRepo(username, reponame);

    document.getElementById("issuestable").innerHTML = "Buscando issues...";
    le_repo.sync.busca_issues("#issuestable");
    le_repo.sync.popula_tabela("#issuestable");
    
}
$.ajaxSetup({ cache: false });