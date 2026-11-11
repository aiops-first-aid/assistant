from huggingface_hub import snapshot_download

snapshot_download(
    repo_id="phamquiluan/RCAEval",
    repo_type="dataset",
    allow_patterns="re1ob*",
    local_dir="data",
)