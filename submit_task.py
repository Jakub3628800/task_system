from tasks import visit_and_summarize

result = visit_and_summarize.delay("https://github.com/Jakub3628800").get()
