from invoke import task


@task
def unit(ctx):
    ctx.run("python manage.py test sh8core")
    ctx.run("python manage.py test web")
    ctx.run("python manage.py test rest")
    ctx.run("python manage.py test recvmail")


@task
def func(ctx):
    # setup
    ctx.run("python manage.py runrecv &")
    ctx.run("python manage.py runbatch &")
    ctx.run("python manage.py runserver &")
    # test
    ctx.run("python manage.py test functional_tests")
    # teardown
    ctx.run("python manage.py runrecv --stop")
    ctx.run("python manage.py runbatch --stop")
    ctx.run("pkill -f \"python manage.py runserver\"")
