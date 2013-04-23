sys.path += ['.']
extensions += ['sphinxcontrib_roles']

# configuration case.1: define roles as list (define only roles)
roles = ['strike', red]


# configuration case.2: define roles as dict (define roles and its style on HTML)
roles = {'strike': "text-decoration: line-through;",
         'red': "color: red;" }
