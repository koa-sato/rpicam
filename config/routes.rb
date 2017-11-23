Rails.application.routes.draw do
  resources :users
  root 'users#index', as: 'home'
  get 'edit' => 'users#edit'
  get 'camera' => 'camera#index'
  # For details on the DSL available within this file, see http://guides.rubyonrails.org/routing.html
end
