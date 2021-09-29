from pathlib import Path
from src.job import Job
CONTENT = "content"

def test_should_create_filelist(tmp_path):
    # FIXME: in questo esempio usa i Path
    d = tmp_path / "sub"
    d.mkdir()
    p = d / "hello.txt"
    p.write_text(CONTENT)
    job = Job(d, "")
    filelist = job.create_filelist()
    assert p.read_text() == CONTENT
    assert len(filelist) == 1, "Filelist should contains exactly one file"
    assert filelist[0].contains(p)