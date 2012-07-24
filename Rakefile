task :deploy do
  puts "Deploying Day"
  sh "python deploy.py day.config"
  puts "Deploying Night"
  sh "python deploy.py day.config"
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
