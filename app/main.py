def format_linter_error(error: dict) -> dict:
    return {new_key: error[old_key]
            for old_key, new_key in
            {"line_number": "line", "column_number": "column",
             "text": "message", "code": "name"}.items()
            if old_key in error} | {"source": "flake8"}


def format_single_linter_file(file_path: str, errors: list) -> dict:
    return {
        "errors": [
            {"line": inf["line_number"], "column": inf["column_number"],
             "message": inf["text"], "name": inf["code"], "source": "flake8"}
            for inf in errors],
        "path": file_path,
        "status": "failed" if errors else "passed"
    }


def format_linter_report(linter_report: dict) -> list:
    return [format_single_linter_file(errors, file_path)
            for errors, file_path in linter_report.items()]
