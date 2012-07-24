task :deploy do
  sh "python deploy.py user.config"
end

task :compass do
  sh("compass compile")  
end

task :clipboard_day do
  sh("cat stylesheets/day.css | pbcopy")
end

task :clipboard_night do
  sh("cat stylesheets/night.css | pbcopy")
end
