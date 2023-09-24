import cx_Freeze

executables = [cx_Freeze.Executable('YoutubeMp4.py')]

cx_Freeze.setup(

    name="Baixar Videos",
    options={'build_exe':{'packages':['pytube','flet'],
                          'include_files':['Downloads.py']}},
executables = executables

)