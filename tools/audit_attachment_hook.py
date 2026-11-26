"""Replay only reviewed CGEE hook template against simulated tool JSON.

The Bash command strings below are DATA: never executed. Source bytes must match
the supplied, read attachment. This tests a regex hook, NOT any installed host sandbox.
"""
from pathlib import Path
import hashlib,json,os,re,subprocess,sys,tempfile
P=Path(__file__).resolve().parents[1]
EXPECTED='571f5311ab243639053fd99c478ef6ebbb11de2cdb83b3858ed0e944e85c3758'

def main():
 path=Path(sys.argv[1]) if len(sys.argv)>1 else P.parent/'uploads/CGEE_R5.5.md'
 raw=path.read_bytes()
 if hashlib.sha256(raw).hexdigest()!=EXPECTED:raise SystemExit('Attachment bytes changed; review new source first, do not auto-refresh EXPECTED.')
 text=raw.decode();blocks=list(re.finditer(r'^```python\n(.*?)^```',text,re.M|re.S))
 match=next(m for m in blocks if 'PROTECTED_WRITE =' in m.group(1))
 code=match.group(1);start=text[:match.start(1)].count('\n')+1
 # These source statements were manually read before this controlled run.
 assert 'subprocess.run(["git",' in code and 'exec(' not in code and 'eval(' not in code
 cases=[
  ('benign_read','Bash',{'command':'cat books/example.txt'},False,0),
  ('write_kb_block_control','Bash',{'command':'echo x > kb/claims.json'},False,2),
  ('write_tools_not_blocked','Bash',{'command':'python -c "from pathlib import Path; Path(\'tools/check.py\').write_text(\'changed\')"'},False,0),
  ('write_dotgithub_not_blocked','Bash',{'command':'echo changed > .github/workflows/check.yml'},False,0),
  ('write_dotclaude_not_blocked','Bash',{'command':'echo changed > .claude/settings.json'},False,0),
  ('draft_read_tests_block_control','Bash',{'command':'cat tests/fixture.py'},True,2),
  ('draft_read_git_block_control','Bash',{'command':'cat .git/config'},True,2),
  ('prose_without_scaffold_block_control','Write',{'file_path':'books/b/chapters/c/c.zh.md','content':'draft'},False,2),
 ]
 runs=[]
 with tempfile.TemporaryDirectory() as td:
  root=Path(td);script=root/'hook.py';script.write_text(code)
  env={**os.environ,'CLAUDE_PROJECT_DIR':str(root)}
  for id,tool,tinp,draft,expected in cases:
   rr=subprocess.run([sys.executable,str(script)],input=json.dumps({'tool_name':tool,'tool_input':tinp,'cwd':str(root)}),cwd=root,env={**env,'CGEE_DRAFTING':'1' if draft else '0'},capture_output=True,text=True,timeout=8)
   runs.append({'id':id,'returncode':rr.returncode,'expected_observation':expected,'matches_expected_observation':rr.returncode==expected,'diagnostic':rr.stderr.strip()[:450]})
  assert not (root/'tools').exists() and not (root/'.github').exists(),'Command payload must remain unexecuted DATA.'
 out={'attachment_sha256':EXPECTED,'source_start_line':start,'extracted_hook_sha256':hashlib.sha256(code.encode()).hexdigest(),
      'all_bash_payloads_are_unexecuted_test_data':True,'runs':runs,'expected_observations_confirmed':all(r['matches_expected_observation'] for r in runs),
      'conclusion':'The supplied regex hook alone permits the three named protected-write forms. Actual OS sandbox, permissions and remote branch controls were NOT tested or bypassed.',
      'status':'template_not_approved_for_deployment'}
 (P/'artifacts/ATTACHMENT_HOOK_AUDIT.json').write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n');print(json.dumps(out,ensure_ascii=False,indent=2));assert out['expected_observations_confirmed']
if __name__=='__main__':main()
