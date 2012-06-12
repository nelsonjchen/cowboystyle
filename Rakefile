task :deploy do
  sh "python deploy.py user.config"
end

task :compass do
  sh("compass compile")  
end

task :clipboard do
  sh("cat stylesheets/style.css | pbcopy")
end
