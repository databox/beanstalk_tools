# beanstalk_tools

Tools that will make your life easier when dealing with beanstalkd.

- [Oto Brglez](https://github.com/otobrglez)

## Deleting jobs

[delete_jobs.py](delete_jobs.py) will delete jobs in beanstalk. It will first peek the next
job and then use picked job id to delete the job. This process is very slow, and to
combat slowness this script uses 5 parallel threads.

```bash
./delete_jobs.py <host> <port> <tube> <type>
```

`type` can either be `buried` or `delayed`.

# License

`MIT`

