# Sobre

...

# Autenticação

...

# Rotas

As seguintes rotas podem ser acessadas sem a necessidade de um token:
/user - POST
/user/login - POST
/result - GET

# Rotas autenticadas

As seguintes rotas necessitam um token:
/user/update/<user_id> - PATCH
/user/delete/<user_id> - DELETE
/all_tickets - GET
/check_result - GET
new_ticket/<tens> - GET
