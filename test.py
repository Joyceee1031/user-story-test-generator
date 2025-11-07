from llm_sandbox import SandboxSession
with SandboxSession(lang="python") as session:
    result = session.run("print('sandbox ok')")
    print(result.stdout)