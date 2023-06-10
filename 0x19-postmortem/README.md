# 0x19. Postmortem

## Description :house:
Any software system will eventually fail, and that failure can come stem from a wide range of possible factors: bugs, traffic spikes, security issues, hardware failures, natural disasters, human error… Failing is normal and failing is actually a great opportunity to learn and improve. Any great Software Engineer must learn from his/her mistakes to make sure that they won’t happen again. Failing is fine, but failing twice because of the same issue is not.<br>A postmortem is a tool widely used in the tech industry. After any outage, the team(s) in charge of the system will write a summary that has 2 main goals:<br>To provide the rest of the company’s employees easy access to information detailing the cause of the outage. Often outages can have a huge impact on a company, so managers and executives have to understand what happened and how it will impact their work.<br>And to ensure that the root cause(s) of the outage has been discovered and that measures are taken to make sure it will be fixed.

## Tasks :pencil:
1<br>Using one of the web stack debugging project issue or an outage you have personally face, write a postmortem. Most of you will never have faced an outage, so just get creative and invent your own :)<br>Requirements:<br>Issue Summary (that is often what executives will read) must contain:<br>duration of the outage with start and end times (including timezone)<br>what was the impact (what service was down/slow? What were user experiencing?<br>How many % of the users were affected?)<br>what was the root cause
Timeline (format bullet point, format: time - keep it short, 1 or 2 sentences) must contain:<br>when was the issue detected
how was the issue detected (monitoring alert, an engineer noticed something, a customer complained…)<br>actions taken (what parts of the system were investigated, what were the assumption on the root cause of the issue)
misleading investigation/debugging paths that were taken<br>which team/individuals was the incident escalated to<br>how the incident was resolved<br>Root cause and resolution must contain:<br>explain in detail what was causing the issue<br>explain in detail how the issue was fixed<br>Corrective and preventative measures must contain:<br>what are the things that can be improved/fixed (broadly speaking)<br>a list of tasks to address the issue (be very specific, like a TODO, example: patch Nginx server, add monitoring on server memory…)<br>Be brief and straight to the point, between 400 to 600 words
<br>
While postmortem format can vary, stick to this one so that you can get properly reviewed by your peers.
<br>
Please, remember that these blogs must be written in English to further your technical ability in a variety of settings.
<br>
[0. My first postmortem](https://docs.google.com/document/d/1dqZYeNkAYnl_hPwVQWCtFVc1CvFpZAPtKx-OIqcLy5k/edit?usp=drivesdk)
