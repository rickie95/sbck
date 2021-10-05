import pytest

from pathlib import Path
from src.job import Job, SamePathException

CONTENT = "content"

def test_create_job_with_src_equal_to_dest_should_raise_err(tmp_path):
    with pytest.raises(SamePathException) as e_info:
        job = Job(tmp_path, tmp_path)
    assert str(e_info.value) == SamePathException.MESSAGE

def test_include_file_with_ext_in_filelist(tmp_path):
    """ 
        Creates `tmp_path/sub/hello.txt` and assert that:
        - filelist contains only `hello.txt`
        - filelist contains the right relative path
        - absolute path of `hello.txt` is correct
        - `hello.txt`'s path is a subpath of absolute path. 
    """
    d = tmp_path / "sub"
    d.mkdir()
    p = d / "hello.txt" # $tmp_path/sub/hello.txt
    p.write_text(CONTENT)
    job = Job(tmp_path, "")

    filelist = job.create_filelist()

    assert p.read_text() == CONTENT, "Created file is not the right path (?)"
    assert len(filelist) == 1, "Filelist should contains exactly one file"
    assert filelist[0] == str(Path.joinpath(Path("sub"), "hello.txt")), "Relative path is wrong"
    assert str(p) == str(tmp_path / "sub" / "hello.txt"), "Absolute path is wrong"
    assert p.is_relative_to(tmp_path), "File is not in a subpath of root"

def test_copy_file_in_dest_directory(tmp_path):
    """
        Test if `tmp_path/source_dir/file.txt` is copied to `tmp_path/destination_dir/file.txt`
    """
    source = tmp_path / "source_dir"
    source.mkdir()

    dest = tmp_path / "destination_dir"
    dest.mkdir()

    file = source / "file.txt"
    file.write_text("Foo content")

    job = Job(source, dest)
    filelist = job.create_filelist()
    job.copy_files()
    
    assert len(filelist) == 1
    assert Path.exists(dest / "file.txt"), "Path doesn't exist"
    assert Path.is_file(dest / "file.txt"), "Path exist but it's not a file"
    assert (dest / "file.txt").read_text() == "Foo content", "File content is corrupt or unavailable"