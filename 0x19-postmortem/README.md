#  0x19. Postmortem
``DevOps`` ``SysAdmin``

<p>The following is the incident report for the Google API infrastructure outage that occurred on April 30, 2013. We understand this service issue has impacted our valued developers and users, and we apologize to everyone who was affected.</p>

    Issue Summary (that is often what executives will read) must contain:
        duration of the outage with start and end times (including timezone)
        what was the impact (what service was down/slow? What were user experiencing? How many % of the users were affected?)
        what was the root cause
    <p>From 6:26 PM to 7:58 PM PT, requests to most Google APIs resulted in 500 error response messages. Google applications that rely on these APIs also returned errors or had reduced functionality. At its peak, the issue affected 100% of traffic to this API infrastructure. Users could continue to access certain APIs that run on separate infrastructures. The root cause of this outage was an invalid configuration change that exposed a bug in a widely used internal library.</p>

    Timeline (format bullet point, format: time - keep it short, 1 or 2 sentences) must contain:
        when was the issue detected
        how was the issue detected (monitoring alert, an engineer noticed something, a customer complained…)
        actions taken (what parts of the system were investigated, what were the assumption on the root cause of the issue)
        misleading investigation/debugging paths that were taken
        which team/individuals was the incident escalated to
        how the incident was resolved
    
    - 6:19 PM: Configuration push begins
    - 6:26 PM: Outage begins
    - 6:26 PM: Pagers alerted teams
    - 6:54 PM: Failed configuration change rollback
    - 7:15 PM: Successful configuration change rollback
    - 7:19 PM: Server restarts begin
    - 7:58 PM: 100% of traffic back online

    Root cause and resolution must contain:
        explain in detail what was causing the issue
        explain in detail how the issue was fixed

    Corrective and preventative measures must contain:
        what are the things that can be improved/fixed (broadly speaking)
        a list of tasks to address the issue (be very specific, like a TODO, example: patch Nginx server, add monitoring on server memory…)

    Be brief and straight to the point, between 400 to 600 words

