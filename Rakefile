task :deploy_day do
  sh "python deploy.py day.config"
end

task :deploy_night do
  # puts "night!!"
  sh "python deploy.py night.config"
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
