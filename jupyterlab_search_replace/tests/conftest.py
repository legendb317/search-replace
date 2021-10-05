import shutil

import pytest

TEST_PATH = "test_lab_search_replace"


@pytest.fixture
def test_content(jp_root_dir):
    full_test_path = jp_root_dir / TEST_PATH
    test_file = full_test_path / "text_1.txt"
    test_file.parent.mkdir(parents=True, exist_ok=True)
    test_file.write_text(
        "\n".join(
            [
                "Unicode strange file, very strange",
                "ü notebook with λ",
                "Is that strange enough?",
            ]
        )
    )

    test_sub_file = full_test_path / "subfolder" / "text_sub.txt"
    test_sub_file.parent.mkdir(parents=True, exist_ok=True)
    test_sub_file.write_text(
        "\n".join(
            [
                "Unicode strange sub file, very strange",
                "ü notebook with ",
                "Is that λ strange enough?",
            ]
        )
    )

    yield full_test_path

    shutil.rmtree(str(full_test_path))