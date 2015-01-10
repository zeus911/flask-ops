curl -sS localhost:8000/run \
    -H 'Accept: application/x-yaml' \
    -d client='local' \
    -d tgt='*' \
    -d fun='test.ping' \
    -d username='adefyer' \
    -d password='112358' \
    -d eauth='pam'
