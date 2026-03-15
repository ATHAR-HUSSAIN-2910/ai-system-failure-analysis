def detect_root_cause(error_count):
    """
    Detect probable root cause from error patterns
    """

    root_cause = "Unknown"

    for error in error_count:

        if "resolve module" in error.lower():
            root_cause = "Missing or unsupported Node.js modules during build"

        elif "build failed" in error.lower():
            root_cause = "Build process failure"

    return root_cause